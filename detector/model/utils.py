import os


def target_names(datatset_path):
        """Get model target names from path.

        It is a convient method. One could keep track of target names
        however, this makes the translation from number to target names
        easier. The following folder structure regarding dataset is assumed:

        dataset/
            langauge/
                laguage_1.txt
                language_2.txt
        """

        # to prevent confusion we avoid using nested listed comprehension
        folders = [f for f in sorted(os.listdir(datatset_path))
                   if os.path.isdir(os.path.join(datatset_path, f))]
        target_names = [folder for folder in folders]
        return target_names
