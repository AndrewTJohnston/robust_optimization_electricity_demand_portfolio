# Written by Andrew Johnston
# May 12, 2015

# Define model data

#####   Shape profiles   #######################################################

# Shape profiles. Average power over time period.
function get_data_shapes(T,N,S,F,num_groups)
    W = zeros(S,T)
    W[ 1,:] = [0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021]
    W[ 2,:] = [0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021,0.021]
    W[ 3,:] = [0.001,0.001,0.002,0.002,0.003,0.004,0.005,0.007,0.009,0.011,0.013,0.016,0.019,0.023,0.026,0.030,0.034,0.038,0.041,0.044,0.046,0.048,0.049,0.050,0.049,0.048,0.046,0.044,0.041,0.038,0.034,0.030,0.026,0.023,0.019,0.016,0.013,0.011,0.009,0.007,0.005,0.004,0.003,0.002,0.002,0.001,0.001,0.001]
    W[ 4,:] = [0.001,0.001,0.002,0.002,0.003,0.004,0.005,0.007,0.009,0.011,0.013,0.016,0.019,0.023,0.026,0.030,0.034,0.038,0.041,0.044,0.046,0.048,0.049,0.050,0.049,0.048,0.046,0.044,0.041,0.038,0.034,0.030,0.026,0.023,0.019,0.016,0.013,0.011,0.009,0.007,0.005,0.004,0.003,0.002,0.002,0.001,0.001,0.001]
    W[ 5,:] = [0.001,0.001,0.002,0.002,0.003,0.004,0.005,0.007,0.009,0.011,0.013,0.016,0.019,0.023,0.026,0.030,0.034,0.038,0.041,0.044,0.046,0.048,0.049,0.050,0.049,0.048,0.046,0.044,0.041,0.038,0.034,0.030,0.026,0.023,0.019,0.016,0.013,0.011,0.009,0.007,0.005,0.004,0.003,0.002,0.002,0.001,0.001,0.001]
    W[ 6,:] = [0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021]
    W[ 7,:] = [0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042]
    W[ 8,:] = [0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063]
    W[ 9,:] = [0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063]
    W[10,:] = [0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042]
    W[11,:] = [0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021,0.042,0.063,0.063,0.042,0.021,0.021]
    W[12,:] = [0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0]
    W[13,:] = [0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0]
    W[14,:] = [0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0]
    W[15,:] = [0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042]
    W[16,:] = [0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042]
    W[17,:] = [0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042,0.042,0.042,0,0,0,0.042]
    return W
end

# Shapes' grouping
function get_data_groups(T,N,S,F,num_groups)
    groups = zeros(num_groups,S)
    groups[ 1,:] = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    groups[ 2,:] = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    groups[ 3,:] = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    groups[ 4,:] = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    groups[ 5,:] = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    groups[ 6,:] = [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0]
    groups[ 7,:] = [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0]
    groups[ 8,:] = [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]
    groups[ 9,:] = [0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]
    groups[10,:] = [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0]
    groups[11,:] = [0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    groups[12,:] = [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0]
    groups[13,:] = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0]
    groups[14,:] = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]
    groups[15,:] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0]
    groups[16,:] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
    groups[17,:] = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
    return groups
end

#####   Nodes' shape coefficients   ###################################################

# Nodes' shape coefficients (nominal)
function get_data_coefficients(T,N,S,F,num_groups)
    K = zeros(N,S)
    K[ 1,:] = [33,52,29,48,13,6,9,6,9,2,0,30,16,78,33,2,14]
    K[ 2,:] = [1,64,31,15,58,3,4,9,17,20,0,25,0,47,30,2,2]
    K[ 3,:] = [10,23,30,14,50,43,1,49,0,1,24,45,30,27,28,5,36]
    K[ 4,:] = [45,65,29,28,36,0,51,5,8,33,7,40,6,48,6,23,29]
    K[ 5,:] = [26,8,4,84,49,4,11,1,35,4,15,10,79,29,12,64,44]
    K[ 6,:] = [81,73,59,64,66,0,11,16,1,15,1,9,82,9,50,27,34]
    K[ 7,:] = [0,9,0,0,0,0,0,0,0,0,0,4,1,0,9,53,0]
    K[ 8,:] = [34,0,10,66,0,0,0,0,0,0,0,34,0,0,0,0,70]
    K[ 9,:] = [5,29,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0]
    K[10,:] = [0,0,0,3,0,0,0,0,0,0,0,0,0,12,0,38,0]
    K[11,:] = [30,40,0,9,0,0,10,0,0,0,0,0,0,30,0,0,0]
    K[12,:] = [5,69,0,0,0,0,0,0,0,0,0,0,26,0,0,0,0]
    K[13,:] = [0,24,55,57,0,0,0,0,0,0,0,13,3,5,25,0,0]
    K[14,:] = [7,0,40,83,0,0,0,0,0,0,0,10,0,0,0,5,29]
    K[15,:] = [18,4,2,14,0,0,0,2,3,15,22,0,0,23,0,0,30]
    K[16,:] = [43,0,24,0,0,17,67,0,30,14,28,0,0,0,4,12,71]
    K[17,:] = [12,0,59,5,26,34,0,0,63,11,10,0,0,52,0,9,12]
    K[18,:] = [40,40,0,23,0,0,0,0,0,0,0,0,30,30,30,30,0]
    K[19,:] = [0,29,0,7,24,0,0,43,6,0,44,0,58,0,0,0,0]
    K[20,:] = [62,0,0,25,0,0,0,0,11,10,0,0,0,9,3,6,0]
    return K
end

#####   Shape sensitivities to factors   ##############################################

# Shape's sensitivities to factors
function get_data_sensitivities(T,N,S,F,num_groups)
    sense = zeros(S,F)
    sense[:,1] = [0.01,0.01,0.50,1.0 ,-0.5,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]
    sense[:,2] = [0.01,0.01,0.01,0.01,   0,0.08,0.08,0.08,0.08,0.08,0.08,0.08,0.08,0.08,0.08,0.08,0.08]
    return sense
end

#####   Means   ###############################################

# Means, factors
function get_data_mean_factors(T,N,S,F,num_groups)
    μ = zeros(F)
    μ = [0,0]
    return μ
end

# Means, errors
function get_data_mean_errors(T,N,S,F,num_groups)
    μ = zeros(N*S)
    return μ
end

#####   Standard deviations   #################################

# Standard deviations, unscaled, shapes
function get_data_stdev_shapes(T,N,S,F,num_groups)
    σ = ones(S)
    return σ
end

# Standard deviations, unscaled, factors
function get_data_stdev_factors(T,N,S,F,num_groups)
    σ = ones(F)
    #σ = [0.2, 0.05]
    return σ
end

# Standard deviations, unscaled, errors
function get_data_stdev_errors(T,N,S,F,num_groups)
    σ = ones(S)
    return σ
end