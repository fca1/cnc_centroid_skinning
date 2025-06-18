import sys

from cnc_centroid_skinning import detect_cnc, CentroidApi

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("please, give in parameter the path of cncn/cnmt program")
        sys.exit(1)
    file_path_of_prg = sys.argv[1]
    detect_cnc(file_path_of_prg)



    sk = CentroidApi(file_path_of_prg)

    burst_mode = sk.burst_mode


    sk.plc.getPcSystemVariableBit(0)

    pass
