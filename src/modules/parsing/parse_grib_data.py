""" parses grib files """
from typing import Dict, List
from pathlib import Path
import xarray

from src.enumerations.unified_forecast_variables import ForecastVariables
from src.modules.config.constants import KEY_LOCAL_FILE_PATHS


def parse_all_variable_files(model_file_list: Dict[str, List[Path]],
                             variable: ForecastVariables) -> xarray.Dataset:
    
    variable_file_list = [file for file in model_file_list[KEY_LOCAL_FILE_PATHS] if variable.value in file]
    return xarray.open_mfdataset(variable_file_list, engine='cfgrib')