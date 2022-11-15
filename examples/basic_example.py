####################################################
#
# This Work is written by Nikolai Rozanov <nikolai>
#
# Contact:  nikolai.rozanov@gmail.com
#
# Copyright (C) 2018-Present Nikolai Rozanov
#
####################################################

####################################################
# IMPORT STATEMENTS
####################################################

# >>>>>>  Native Imports  <<<<<<<

# >>>>>>  Package Imports <<<<<<<

# >>>>>>  Local Imports   <<<<<<<
from annotation_analysis import interannotator_metrics

####################################################
# CODE
####################################################







####################################################
# MAIN
####################################################
if __name__ == "__main__":
    annotations = [["A","B","A"],["A","B","B"]]
    k_alpha = interannotator_metrics.krippendorff_alpha(annotations)
    f_kappa = interannotator_metrics.fleiss_kappa(annotations)
    print(k_alpha)
    print(f_kappa)


# EOF
