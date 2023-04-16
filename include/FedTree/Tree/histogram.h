#ifndef FEDTREE_HISTOGRAM_H
#define FEDTREE_HISTOGRAM_H

#include "hist_cut.h"

class Histogram{
    vector<HistCut> cut;
    SyncArray<GHPair> histogram;
};

#endif //FEDTREE_HISTOGRAM_H
