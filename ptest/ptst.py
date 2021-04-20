# This is a test program for the ncglm python wrappers.

# Maximilian McClelland 1/29/21

# This works on my local machine but seemed not to on Ed's. Need to figure out why that is.
import psrc.ncglm
import time

EPSILON = 0.0001
NUM_VAL = 5


def main():
    print("TestingPythonWrapper\n")
    print("Testing GLM event reads.")
    glm_event()
    print("Testing GLM flash reads.")
    glm_flash()
    print("Testing GLM group reads.")
    glm_group()


def glm_event():
    global EPSILON
    global NUM_VAL
    total_err = 0
    err = 0
    print("testing GLM event reads...")
    x_time = [-0.475699, -0.475699, -0.444037, -0.332646, -0.330739]
    x_lat = [23.9904, 23.9945, 23.9904, 23.9904, 23.9904]
    x_lon = [-105.711212, -105.619804, -105.711212, -105.711212, -105.711212]
    x_energy = [1.37337e-14, 7.62985e-15, 3.05194e-15, 4.57791e-15, 4.57791e-15]
    x_parent_group_id = [467109464, 467109464, 467109465, 467109472, 467109473]

    i = 0
    ret = 0


def glm_flash():
    print("testing GLM flash reads...")
    total_err = 0
    err = 0
    ncid = 0
    ret = 0


def glm_read():
    print("Reading Geostationary Lightning Mapper data")


def glm_group():
    print("testing GLM group reads...")


def are_same(a, b):
    if fabs(a - b) < EPSILON:
        return 1
    else:
        return 0


def fabs(equation):
    return equation


def print_time(offset):
    print(time.asctime(time.localtime(time.time() + offset)))

def show_att(ncid, varid, name):

    return 0

main()
