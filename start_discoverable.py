import subprocess


def start_discoverable():
    """
    raspberrypi��ble�ł̓Z�L�����e�B�̊ϓ_���炩�Cble�����ɂ�����Ȃ��悤�ɂȂ��Ă���̂ŁC����I�Ɉȉ��̃R�}���h�����s����K�v������.
    �܂�T�[�o�[�Ƃ��ď����󂯎�邽�߂ɂ͈ȉ��̃R�}���h�𖈉�s���K�v������̂ŁC�T�[�o���N������Ƃ��Ɉȉ��̃R�}���h�������I�Ɏ��s����悤�ɕύX����K�v������D
    �ȉ��R�}���h���C�T�[�o�N���O�Ɏ��s����K�v������̂ŁC�֐�������D
    $ bluetoothctl
    $ discoverable on
    """
    subprocess.run(['sudo','bluetoothctl','discoverable','on'])


start_discoverable()