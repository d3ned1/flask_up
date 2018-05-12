# coding=utf-8
import os, re


def check_for_update(update_directory):
    try:
        os.chdir(update_directory)
        last_available_version = '.'.join(re.split('[.]', sorted(os.listdir(os.getcwd()))[-1])[:-2])
        last_patch_version = '.'.join(re.split('[.]', sorted(os.listdir(os.getcwd()))[-1])[1:3])
        return {'last_available_version': last_available_version, 'last_patch_version': last_patch_version}
    except Exception as e:
        exception = str(e)
        return {'exception': exception}