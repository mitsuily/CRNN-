#!/bin/sh

BIN_PATH=/root/pvc2/build/install/bin/
ITER=$1

if [ -z "${ITER}" ]; then
  ${BIN_PATH}/caffe train --solver=solver.prototxt
else
  ${BIN_PATH}/caffe train --solver=solver.prototxt --snapshot=densenet-sum-blstm-full-res-blstm_iter_${ITER}.solverstate
fi
