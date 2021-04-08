# Just to keep track

using Pkg
ENV["JULIA_CUDA_USE_BINARYBUILDER"] = "false"

# Required
Pkg.add("IJulia")
Pkg.add("Flux")
Pkg.add("AbstractPlotting")
Pkg.add("GLMakie")
Pkg.add("Colors")
Pkg.add("CairoMakie")
Pkg.add("DifferentialEquations")

# Extras
# Fancy extra things
# Pkg.add("https://github.com/ffreyer/SphereSurfaceHistogram.jl.git")


# Mentioned
# These haven't been used but are relevant to some tasks/notes
# Pkg.add("https://github.com/janattig/LatPhysBase.jl")
# Pkg.add("https://github.com/janattig/LatPhysUnitcellLibrary.jl")
# Pkg.add("https://github.com/janattig/LatPhysLatticeConstruction.jl")
# Pkg.add("https://github.com/janattig/LatPhysLatticeModification.jl")
# Pkg.add("https://github.com/janattig/LatPhysReciprocal.jl")
# Pkg.add("https://github.com/janattig/LatPhysBandstructures.jl")
# Pkg.add("https://github.com/janattig/LatPhysLuttingerTisza.jl")
# Pkg.add("https://github.com/janattig/LatticePhysics.jl")
# Pkg.add("StaticArrays")