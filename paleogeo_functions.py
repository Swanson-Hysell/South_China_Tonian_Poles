import numpy as np
import xml.etree.ElementTree as ET
import matplotlib.patches as patches
import cartopy.crs as ccrs
import pmagpy.pmag as pmag
import pmagpy.ipmag as ipmag


def rotated_pole_plot(ax, plon, plat, a95, Eulers, marker='o', s=20, marker_color='r', alpha=0.6):
    """
    Plot paleomagnetic pole with rotation using ipmag.plot_pole().
    """
    # rotate pole
    rotated_plat = plat
    rotated_plon = plon
    for i in range(len(Eulers)):
        rotated_plat, rotated_plon = pmag.pt_rot(Eulers[i], [rotated_plat], [rotated_plon])
        rotated_plat = rotated_plat[0]
        rotated_plon = rotated_plon[0]

    # plot pole and a95 using ipmag.plot_pole
    ipmag.plot_pole(ax, rotated_plon, rotated_plat, a95, color=marker_color, 
                    label='', marker=marker, markersize=s,  A95_alpha=alpha, outline=False)
    return rotated_plon, rotated_plat


def rotated_kent_pole_plot(ax, kent_dict, Eulers, marker='o', s=20, marker_color='r', alpha=0.6, lower=False):
    """
    Plot Kent mean paleomagnetic pole with rotation.
    """
    dec = kent_dict['dec']
    inc = kent_dict['inc']
    Zdec = kent_dict['Zdec']
    Zinc = kent_dict['Zinc']
    Edec = kent_dict['Edec']
    Einc = kent_dict['Einc']
    Zeta = kent_dict['Zeta']
    Eta = kent_dict['Eta']

    # rotate pole
    for i in range(len(Eulers)):
        inc, dec = pmag.pt_rot(Eulers[i], [inc], [dec])
        Zinc, Zdec = pmag.pt_rot(Eulers[i], [Zinc], [Zdec])
        Einc, Edec = pmag.pt_rot(Eulers[i], [Einc], [Edec])

        dec = dec[0]
        inc = inc[0]
        Zdec = Zdec[0]
        Zinc = Zinc[0]
        Edec = Edec[0]
        Einc = Einc[0]
    
    rotated_dict = {'dec': dec, 'inc': inc, 'Zdec': Zdec, 'Zinc': Zinc, 'Edec': Edec, 'Einc': Einc, 'Zeta': Zeta, 'Eta': Eta}
    ipmag.plot_pole_ellipse(ax, rotated_dict, 
                            color = marker_color,
                            edgecolor = 'k',
                            marker = marker,
                            markersize = s,
                            label = '',
                            alpha = alpha,
                            lower= lower,
                            zorder= 100)
    return ax


def craton_plot(ax, plateIDs, Eulers, edgecolor, facecolor, alpha, linewidth, 
                gpml = 'shapes_cratons.gpml', reverse_draw=False):
    """
    Plot cratons with rotation.
    
    Parameters
    ----------
    ax : map axis
        On which to plot.
    
    plateIDs : list
        Of plateIDs.
        
    Eulers : list of lists
        Of Euler rotation parameters - if more than one given,
        the rotations will be additive.
    """
    # get cratons from .gpml

    Xs, Ys = get_craton_XYs(gpml, plateIDs)
    
    # draw in reverse
    if reverse_draw:
        Xs = np.flip(Xs)
        Ys = np.flip(Ys)
    
    # rotate cratons
    rotated_Xs = []
    rotated_Ys = []
    for i in range(len(Xs)):
        rotated_X = np.array([])
        rotated_Y = np.array([])
        for j in range(len(Xs[i])):
            this_X = [Xs[i][j]]
            this_Y = [Ys[i][j]]
            for k in range(len(Eulers)):
                this_Y, this_X = pmag.pt_rot(Eulers[k], this_Y, this_X)
            rotated_X = np.append(rotated_X, this_X)
            rotated_Y = np.append(rotated_Y, this_Y)
        rotated_Xs.append(rotated_X)
        rotated_Ys.append(rotated_Y)
        
    # add cratons
    for i in range(len(rotated_Xs)):
        XY = np.stack([rotated_Xs[i][::-1],rotated_Ys[i][::-1]],axis=1)
        poly_edge = patches.Polygon(XY,
                                    edgecolor=edgecolor,facecolor='none',alpha=alpha,
                                    transform=ccrs.Geodetic(), linewidth=linewidth)
        poly_face = patches.Polygon(XY,
                                    edgecolor='none',facecolor=facecolor,alpha=alpha,
                                    transform=ccrs.Geodetic())
        ax.add_patch(poly_face)
        ax.add_patch(poly_edge)


def get_craton_XYs(gpml, plateIDs):
    """
    Get XY coordinates of a plate polygon from a .gpml.
    
    Parameters
    ----------
    gpml : string
        Path to .gpml file.
        
    plateIDs : list
        Of plateIDs.
    """
    # namespace dictionary
    ns = {'gpml':'http://www.gplates.org/gplates',
          'gml':'http://www.opengis.net/gml'}
    
    # initial parse
    tree = ET.parse(gpml)
    root = tree.getroot()
    
    # storage
    Xs = []
    Ys = []
    
    # iterate through featureMembers
    for featureMember in root.findall('gml:featureMember',ns):
        
        # get child
        for child in featureMember:
            slice_ind = child.tag.find('}')
            child_root = 'gpml:' + child.tag[slice_ind+1:]
        
        # check plateID
        plateID_path = child_root + '/gpml:reconstructionPlateId/gpml:ConstantValue/gpml:value'
        feature_plateID = int(featureMember.find(plateID_path,ns).text)
        if feature_plateID in plateIDs:
            
            if featureMember.find(child_root + '/gpml:outlineOf', ns)!=None:
                polygon_root = child_root + '/gpml:outlineOf'
            elif featureMember.find(child_root + '/gpml:boundary', ns)!=None:
                polygon_root = child_root + '/gpml:boundary'
            elif featureMember.find(child_root + '/gpml:unclassifiedGeometry', ns)!=None:
                polygon_root = child_root + '/gpml:unclassifiedGeometry'
            elif featureMember.find(child_root + '/gpml:centerLineOf', ns)!=None:
                polygon_root = child_root + '/gpml:centerLineOf'
            else:
                raise Exception('polygon_root undefined.')
            
            # get coordinates
            posList_path = polygon_root + '/gpml:ConstantValue/gpml:value/gml:Polygon/gml:exterior/gml:LinearRing/gml:posList'
            for feature_posList in featureMember.findall(posList_path,ns):
                np_posList = np.fromstring(feature_posList.text, dtype=float, sep=' ')
            
                # split into lat and lon
                lat_inds = np.arange(0, len(np_posList), 2, dtype=int)
                lon_inds = np.arange(1, len(np_posList), 2, dtype=int)

                feature_lat = np_posList[lat_inds]
                feature_lon = np_posList[lon_inds]
            
                Xs.append(feature_lon)
                Ys.append(feature_lat)
            
    return Xs, Ys