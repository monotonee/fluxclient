import cython
from libcpp.vector cimport vector

import fluxclient.scanner.scan_settings as scan_settings


cdef extern from "scan_module.h":
    cdef cppclass PointCloudXYZRGBPtr:
        pass
    cdef cppclass NormalPtr:
        pass
    cdef cppclass PointXYZRGBNormalPtr:
        pass
    cdef cppclass MeshPtr:
        pass

    PointCloudXYZRGBPtr createPointCloudXYZRGB()
    NormalPtr createNormalPtr()
    MeshPtr createMeshPtr()
    int loadPointCloudXYZRGB(const char* file, PointCloudXYZRGBPtr cloud)
    void dumpPointCloudXYZRGB(const char* file, PointCloudXYZRGBPtr cloud)
    void push_backPoint(PointCloudXYZRGBPtr cloud, float x, float y, float z, cython.uint rgb)
    int get_item(PointCloudXYZRGBPtr cloud, int key, vector[float] point)
    int get_w(PointCloudXYZRGBPtr cloud)

    # void push_backPoint(PointCloudXYZRGBPtr cloud, float x, float y, float z)

    int SOR(PointCloudXYZRGBPtr cloud, int neighbors, float thresh)
    int VG(PointCloudXYZRGBPtr cloud)

    int ne(PointCloudXYZRGBPtr cloud, NormalPtr normals, float radius)
    int ne_viewpoint(PointCloudXYZRGBPtr cloud, NormalPtr normals, float radius, vector[vector [float]] viewp, vector[int] step)
    # int ne_viewpoint(PointCloudXYZRGBPtr cloud, NormalPtr normals, vector[float] viewp, vector[int] step)
    PointXYZRGBNormalPtr createPointXYZRGBNormalPtr()
    PointXYZRGBNormalPtr concatenatePointsNormal(PointCloudXYZRGBPtr cloud, NormalPtr normals)
    PointCloudXYZRGBPtr POS(PointXYZRGBNormalPtr cloud_with_normals, MeshPtr triangles);

    int STL_to_Faces(MeshPtr, vector[vector [int]] &viewp)

cdef class PointCloudXYZRGBObj:
    cdef PointCloudXYZRGBPtr obj
    cdef NormalPtr normalObj
    cdef PointXYZRGBNormalPtr bothobj
    cdef MeshPtr meshobj

    def __init__(self):
        self.obj = createPointCloudXYZRGB()
        self.normalObj = createNormalPtr()
        self.meshobj = createMeshPtr()

    def get_w(self):
        return get_w(self.obj)

    cpdef loadFile(self, unicode filename):
        if loadPointCloudXYZRGB(filename.encode(), self.obj) == -1:
            raise RuntimeError("Load failed")

    cpdef PointCloudXYZRGBObj clone(self):
        cdef PointCloudXYZRGBObj obj = PointCloudXYZRGBObj()
        # TODO:
        raise RuntimeError("Not implement clone yet")
        # return obj

    cpdef dump(self, unicode filename):
        dumpPointCloudXYZRGB(filename.encode(), self.obj)

    cpdef push_backPoint(self, float x, float y, float z, cython.uint rgb):
        # TODO: put r,g,b -> rgb in here
        push_backPoint(self.obj, x, y, z, rgb)

    cpdef get_item(self, key):
        cdef vector[float] point = [0., 0., 0., 0., 0., 0.]
        assert key < self.get_w(), 'get index:%d out of range:%d' % (key, self.get_w())
        get_item(self.obj, key, point)
        return point

    cpdef int SOR(self, int neighbors, float threshold):
        return SOR(self.obj, neighbors, threshold)

    cpdef int VG(self):
        return VG(self.obj)

    cpdef int ne(self):
        return ne(self.obj, self.normalObj, 0.5)

    cpdef int ne_viewpoint(self, viewp, step):

        cdef vector[vector[float]] vect1
        cdef vector[float] vect2

        for i in viewp:
            vect2.clear()
            # vect2 = new vector[int]()
            for j in i:
                vect2.push_back(j)
            vect1.push_back(vect2)
        viewp = vect1


        cdef vector[int] vect
        for i in step:
            vect.push_back(i)
        step = vect

        return ne_viewpoint(self.obj, self.normalObj, 1.0, viewp, step)
        # return ne_viewpoint(self.obj, self.normalObj, step)

    cpdef int concatenatePointsNormal(self):
        self.bothobj = concatenatePointsNormal(self.obj, self.normalObj)
        return 0

    cpdef to_mesh(self):
        self.concatenatePointsNormal()

        new_c = PointCloudXYZRGBObj()
        new_c.obj = POS(self.bothobj, self.meshobj)
        return new_c


    cpdef STL_to_Faces(self):
        cdef vector[vector [int]] viewp
        STL_to_Faces(self.meshobj, viewp)
        return viewp




# reg part
cdef extern from "scan_module.h":

    cdef cppclass PointNT:
        pass
    cdef cppclass M4f: # Eigen::Matrix4f (might cause namespace error)
        pass
    cdef cppclass FeatureCloudTPtr:
        pass


    int loadPointNT(const char* file, PointXYZRGBNormalPtr cloud)
    void dumpPointNT(const char* file, PointXYZRGBNormalPtr cloud)
    int FE(PointXYZRGBNormalPtr cloud, FeatureCloudTPtr cloud_features, float radius)
    int SCP(PointXYZRGBNormalPtr object, FeatureCloudTPtr object_features, PointXYZRGBNormalPtr scene, FeatureCloudTPtr scene_features, M4f &transformation, float leaf)


cdef class RegCloud:
    cdef PointXYZRGBNormalPtr scene, obj
    cdef FeatureCloudTPtr scene_f, obj_f
    cdef M4f transformation

    def __init__(self):
        self.obj = createPointXYZRGBNormalPtr()
        self.scene = createPointXYZRGBNormalPtr()

    cpdef loadFile(self, unicode filename_scene, unicode filename_obj):
        if loadPointNT(filename_scene.encode(), self.scene) == -1:
            raise RuntimeError("Load failed")
        if loadPointNT(filename_obj.encode(), self.obj) == -1:
            raise RuntimeError("Load failed")

    cpdef dump_o(self, unicode filename):
        dumpPointNT(filename.encode(), self.obj)

    cpdef dump_s(self, unicode filename):
        dumpPointNT(filename.encode(), self.scene)

    cpdef dump(self, unicode filename_1, unicode filename_2):
        self.dump_o(filename_1)
        self.dump_s(filename_2)

    cpdef int FE(self, float radius):
        return FE(self.scene, self.scene_f, radius) & FE(self.obj, self.obj_f, radius)

    cpdef int SCP(self, float leaf = 2.0):
        return SCP(self.obj, self.obj_f, self.scene, self.scene_f, self.transformation, leaf)
