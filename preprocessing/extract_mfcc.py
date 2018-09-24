import logging
import os
from os.path import join
import sys

speech_file_name = "speech_fragment.wav"
output_file_name = "output_timestamp.csv"


def extract_mfcc_opensmile(conf_file, input_folder_path):

    for subfolder_name in os.listdir(input_folder_path):
        subfolder_path = join(input_folder_path, subfolder_name)
        speech_file_path = join(subfolder_path, speech_file_name)
        logging.info("Reading file:" + speech_file_path)
        os.remove(join(subfolder_path, output_file_name))
        os.remove(join(subfolder_path, "output.csv"))
        os.system("SMILExtract_Release -C " + conf_file + " -I " +
                  speech_file_path + " -outputfile " +
                  join(subfolder_path, output_file_name))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        filename="extract_mfcc.log",
                        format='%(asctime)s %(levelname)s %(message)s')
    logging.info("Starting script")
    conf_file = sys.argv[1]
    input_folder_path = sys.argv[2]
    extract_mfcc_opensmile(conf_file, input_folder_path)
