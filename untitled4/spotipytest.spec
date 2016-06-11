# -*- mode: python -*-

block_cipher = None


a = Analysis(['spotipytest.py'],
             pathex=['C:\\Users\\Boyen\\PycharmProjects\\untitled4'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += [('api.ini', 'api.ini', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='spotipytest',
          debug=False,
          strip=False,
          upx=True,
          console=True )