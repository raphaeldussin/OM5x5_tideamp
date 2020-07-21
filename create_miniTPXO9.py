import xarray as xr

harmonics = ["m2", "s2", "n2", "k2", "k1", "o1", "p1", "q1"]
tpxodir = '/net2/rnd/TPXO/'

tpxo_gridfile = f'{tpxodir}/TPXO9/grid_tpxo9_atlas_30_v2.nc'
ds = xr.open_dataset(f'{tpxodir}/TPXO9/grid_tpxo9_atlas_30_v2.nc')
out = ds.isel(ny=slice(0,-1)).coarsen(nx=60, ny=60).mean()
out.to_netcdf(f'data/grid_tides_2x2.nc', format='NETCDF3_64BIT')

for harm in harmonics:
    ds = xr.open_dataset(f'{tpxodir}/TPXO9/u_{harm}_tpxo9_atlas_30_v2.nc')
    out = ds.isel(ny=slice(0,-1)).coarsen(nx=60, ny=60).mean()
    out.to_netcdf(f'data/u_{harm}_tides_2x2.nc', format='NETCDF3_64BIT')


raw = xr.open_dataset('/archive/gold/datasets/OM4_025/mosaic.v20170622.unpacked/ocean_static.nc')
modelgrid = xr.Dataset()
modelgrid['geolon'] = raw['geolon'].copy()
modelgrid['geolat'] = raw['geolat'].copy()
minigrid = modelgrid.coarsen(xh=20, yh=20).mean()
minigrid.to_netcdf('data/ocean_static_5x5.nc', format='NETCDF3_64BIT')
