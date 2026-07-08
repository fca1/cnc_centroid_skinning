import sys

from cnc_centroid_skinning import detect_cnc


def main():
    if len(sys.argv) < 2:
        print("please, give in parameter the path of cncn/cnmt program")
        return 1
    file_path_of_prg = sys.argv[1]
    return 0 if detect_cnc(file_path_of_prg) else 1


if __name__ == "__main__":
    sys.exit(main())
