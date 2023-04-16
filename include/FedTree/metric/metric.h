#ifndef FEDTREE_METRIC_H
#define FEDTREE_METRIC_H


#include "FedTree/syncarray.h"
#include "FedTree/dataset.h"

class Metric {
public:
    virtual float_type get_score(const SyncArray<float_type> &y_p) const = 0;

    virtual void configure(const GBDTParam &param, const DataSet &dataset);

    static Metric *create(string name);

    virtual string get_name() const = 0;

protected:
    SyncArray<float_type> y;
};


#endif //FEDTREE_METRIC_H
