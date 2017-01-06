def combinePasture(vertices):
    bl_01_X = vertices[0]
    bl_01_Y = vertices[1]
    bl_02_X = vertices[4]
    bl_02_Y = vertices[5]
    tr_01_X = vertices[2]
    tr_01_Y = vertices[3]
    tr_02_X = vertices[6]
    tr_02_Y = vertices[7]
    length = max(tr_01_X, tr_02_X, bl_01_X, bl_02_X) - min(tr_01_X, tr_02_X, bl_01_X, bl_02_X)
    height = max(tr_01_Y, tr_02_Y, bl_01_Y, bl_02_Y) - min(tr_01_Y, tr_02_Y, bl_01_Y, bl_02_Y)
    area = pow(max(length, height), 2)
    return area