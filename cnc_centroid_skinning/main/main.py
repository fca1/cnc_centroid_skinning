import sys

from cnc_centroid_skinning import detect_cnc, CentroidApi

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("please, give in parameter the path of cncn/cnmt program")
        sys.exit(1)
    file_path_of_prg = sys.argv[1]
    detect_cnc(file_path_of_prg)
    pass
