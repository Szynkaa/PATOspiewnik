# -*- coding: utf-8 -*-

import sys
import os
import re
import io


def main():
    """"""
    
    #compile_songs.pattern = u"\\newpage\\label{{song:{0}}}\\input{{{0}}}"
    main.pattern = u"\\newpage\\input{{{0}}}"

    working_dir = os.getcwd()


    input_dirs = ["discopolo", "memy", "obce", "poezja", "polskie", "szanty", "szlagiery"]

    # iter over dir
    for input_dir in input_dirs:
        fls = []

        for subdir, dirs, files in sorted(os.walk("piosenki"+os.sep+input_dir), key=lambda path: path[2]):
            for file in sorted(files):
                # print os.path.join(subdir, file)
                filepath = subdir + os.sep + file

                if filepath.endswith(".tex"):
                    fls.append(main.pattern.format(
                        filepath.replace("\\", "/"))
                    )

        result = u"\n".join(fls)

        output_path = working_dir+os.sep+"piosenki"+os.sep+input_dir+".tex"

        with io.open(output_path, mode='w', encoding="utf8") as f:
            f.write(result)

        print("File {0} containing song list created".format(input_dir+".tex"))


if __name__ == '__main__':
    main()
