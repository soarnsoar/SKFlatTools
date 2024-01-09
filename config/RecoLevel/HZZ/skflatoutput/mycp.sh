rm -f combine.root
arr_year=(2016postVFP 2016preVFP 2017 2018)
for year in ${arr_year[@]};do
    mkdir -p ${year}
    cp /data6/Users/jhchoi/SKFlatOutput//Run2UltraLegacy_v3/HZZ_test/${year}/DATA/*.root ${year}/
    cp /data6/Users/jhchoi/SKFlatOutput//Run2UltraLegacy_v3/HZZ_test/${year}/*.root ${year}/
    
done

hadd -f combine3yr.root 201*/*.root
