import enum


class HostStatus(enum.IntEnum):
    ready = 0
    busy = 1
    full = 2


class JobStatus(enum.IntEnum):
    void = 0
    pend = 1
    run = 2
    susp = 3
    done = 4
    exit = 5
    known = 6
