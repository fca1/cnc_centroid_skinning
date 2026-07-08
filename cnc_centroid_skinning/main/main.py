import sys

from cnc_centroid_skinning import detect_cnc


def main():
    if len(sys.argv) < 2:
        print("Please provide the CNC12 installation path.")
        return 1
    file_path_of_prg = sys.argv[1]
    return 0 if detect_cnc(file_path_of_prg) else 1


if __name__ == "__main__":
    sys.exit(main())
