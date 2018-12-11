import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2_timing_cff import Phase2_timing
from Configuration.Eras.Modifier_phase2_timing_layer_cff import phase2_timing_layer
from Configuration.Eras.Modifier_phase2_timing_layer_tile_cff import phase2_timing_layer_tile

Phase2_timing_layer_tile = cms.ModifierChain(Phase2_timing, phase2_timing_layer, phase2_timing_layer_tile)

