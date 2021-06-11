function val = evalFuzzy(x1,x2,x3,x4,x5,x6,x7,x8,x9)
    fis = readfis('project.fis')
    input = [x1 x2 x3 x4 x5 x6 x7 x8 x9];
    val = evalfis(fis,input)
end