import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *


generator = cms.EDFilter("Pythia8GeneratorFilter",
        comEnergy = cms.double(13000.0),
        crossSection = cms.untracked.double(1.095e-3),
        filterEfficiency = cms.untracked.double(1),
        maxEventsToPrint = cms.untracked.int32(0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'HardQCD:gg2gg = on',
            'HiggsSM:gg2H = on',
            '35:onMode = off',
            '35:onIfMatch = 24 -37',
            '35:onIfMatch = -24 37',
            '-37:onMode = off',
            '-37:onIfMatch = -24 25',
            '37:onMode = off',
            '37:onIfMatch = 24 25',
            '25:onMode = off',
            '25:onIfMatch = 5 -5',
            '24:onMode = off',
            '24:onIfMatch = -2 1',
            '24:onIfMatch = -4 3',
            '-24:onMode = off',
            '-24:onIfAny = -11 -12 -13 -14 -15 -16',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
)

ProductionFilterSequence = cms.Sequence(generator)
