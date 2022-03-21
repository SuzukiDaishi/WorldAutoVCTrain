import glob, shutil, os

INPUT_PATH = 'jvs_ver1/*/parallel100/wav24kHz16bit/*.wav'
OUTPUT_PATH = 'jvs/'

def convertName(name):
    return f'j{name[3:]}'

def convertWave(name, wave):
    return f'{name}{wave[len("VOICEACTRESS100"):]}'

def getData(gpath):
    for gp in sorted(glob.glob(gpath)):
        print(gp)
        name = gp.split('/')[-4]
        wave = gp.split('/')[-1]
        name = convertName(name)
        wave = convertWave(name, wave)
        os.makedirs(os.path.join(OUTPUT_PATH, name), exist_ok=True)
        shutil.copy(gp, os.path.join(OUTPUT_PATH, name, wave))
        print(gp, '->', os.path.join(OUTPUT_PATH, name, wave))

if __name__ == '__main__':
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    getData(INPUT_PATH)