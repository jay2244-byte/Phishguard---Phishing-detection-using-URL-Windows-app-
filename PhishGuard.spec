
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    [r'C:\VS Studio code programs\Phishguard windows\main.py'],
    pathex=[r'C:\VS Studio code programs\Phishguard windows'],
    binaries=[],
    datas=[
        (r'C:\VS Studio code programs\Phishguard windows\resources', 'resources'),
        (r'C:\VS Studio code programs\Phishguard windows\database', 'database'),
    ],
    hiddenimports=['win32api', 'win32con', 'win32gui'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PhishGuard',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # Remove the icon parameter since SVG is not supported by PyInstaller
)
