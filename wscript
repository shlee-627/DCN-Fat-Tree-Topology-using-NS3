## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    obj = bld.create_ns3_program('dcn-fatTree',
                                 ['point-to-point', 'applications', 'internet', 'flow-monitor', 'netanim'])
    obj.source = 'DCN_FatTree.cc'
