import os
import random
import uuid

import numpy as np
import py
import scipy.signal
import configparser

from asammdf import MDF, Signal

# Fake Channels and associated unit.
channels = {
    "engine_speed": "rpm",
    "engine_speed_desired": "rpm",
    "vehicle_speed": "kph",
    "transmission_gear": "uint8",
    "coolant_temp": "C",
    "longitude": "",
    "latitude": "",
    "power": "W",
    "efficiency": "[unitless]",
    "X": "",
    "Y": "",
}

# Fake companies
companies = [
    "HeavyEquipmentInc",
    "CarCompanyLLC",
    "HeavyDutyTruckCorp",
    "AerospaceStartup",
]

# Fake Products
products = [
    "Bulldozer",
    "DumpTruck",
    "Excavator",
    "Transmission",
    "Airplane",
]

# Versions of MDF to save data as.
versions = [
    '2.00',
    '2.10',
    '2.14',
    '3.00',
    '3.10',
    '3.20',
    '3.30',
    '4.00',
    '4.10',
    '4.11',
]

# Sample Time Data Generation
## Total signal time
tf = 86400
# Multiple time vectors
t5En1 = np.arange(0, tf, 5e-1, dtype=np.float32)
t1En3 = np.arange(0, tf, 1e-3, dtype=np.float32)
# List of all possible time vectors.
timestamps = [t5En1, t1En3]


def sine(t, A=1, f=1):
    """SINE
    
    """
    sine_ = A * np.sin(
        2 * np.pi * f * t
    )
    return sine_


def cos(t, A=1, f=1):
    """COSINE
    
    """
    cos_ = A * np.sin(
        2 * np.pi * f * t
    )
    return cos_


def square(t, A=1, f=1):
    """SQUARE
    
    """
    square_ = A * scipy.signal.square(
        2 * np.pi * f * t
    )
    return square_


def sawtooth(t, A=1, f=1):
    """SAWTOOTH
    
    """
    sawtooth_ = A * scipy.signal.sawtooth(
        2 * np.pi * f * t,
        width=1,
    )
    return sawtooth_


def triangle(t, A=1, f=1):
    """TRIANGLE
    """
    triangle_ = A * scipy.signal.sawtooth(
        2 * np.pi * f * t,
        width=0.5,
    )
    return triangle_

# List with each of the signal generator types.
signal_generators = [sine, cos, square, sawtooth, triangle]


def random_data():
    signals = list()
    for channel_name, channel_units in channels.items():
        if isinstance(channel_units, str):
            channel_unit = channel_units
        else:
            raise type(channel_units)

        signal_generator = random.choice(signal_generators)

        A = random.randint(1, 10)
        f = random.randint(1, 100)
        T = random.choice(timestamps)
        Y = signal_generator(T, A, f)

        signal_ = Signal(
            samples=Y,
            timestamps=T,
            name=channel_name,
            unit=channel_unit,
        )
        signals.append(signal_)

    company = random.choice(companies)
    product = random.choice(products)
    version = random.choice(versions)

    data_file_uuid = str(uuid.uuid4())

    channel_path_ = ["Data", company, product, data_file_uuid]

    channel_path = py.path.local(
        os.path.join(*channel_path_)
    )
    channel_path.dirpath().ensure(dir=True)

    mdf = MDF(
        version=version,
    )
    mdf.append(
        signals=signals,
        common_timebase=False,
    )
    o = mdf.save(
        dst=str(channel_path),
        overwrite=True,
        compression=2,
    )
    return o
