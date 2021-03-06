# AUTOGENERATED! DO NOT EDIT! File to edit: 00_wigglesphere.ipynb (unless otherwise specified).

__all__ = ['dist_from_point', 'lines_to_layer', 'layer_to_lines']

# Cell
def dist_from_point(line, point):
    '''calculate euclidean distance of a set of points from a reference point'''
    return ((line - point) ** 2).sum(axis=1) ** 0.5

# Cell
def lines_to_layer(lines):
    nanlines = []
    for line in lines:
        _line = np.concatenate([line,np.array([[np.nan, np.nan]])])
        nanlines.append(_line)
    nanlines = np.concatenate(nanlines)
    x = nanlines[:,0]
    y = nanlines[:,1]
    return (x,y)

# Cell
def layer_to_lines(layer):
    _layer = layer[1:,:]  # drop first row containing placeholder nan
    isnan = np.isnan(_layer[:,0]).nonzero()[0]
    lines = []
    start_ind = 0
    for nan_ind in isnan:
        line = _layer[start_ind:nan_ind,:]
        lines.append(line)
        start_ind = nan_ind + 1
    return lines