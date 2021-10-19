#coding=utf-8
#auth:lee
import zipfile

z = zipfile.ZipFile(r'D:\2021\1test\BuuCtf\misc\cjdbmzh.zip', 'r', zipfile.ZIP_DEFLATED)
# if z.testzip() == None:
#     print("校验zip中CRC32完成,无损坏文件")
# else:
#     print("损坏文件名为：",z.testzip())

for info in z.infolist():
    print("文件名",info.filename,'CRC32值：',format(info.CRC & 0xFFFFFFFF, '08x'))

# 使用python  crc32.py reverse 0xccca7e74 解出密钥，然后拼接
passwd1 = ['05J728',
'2ysXnu',
'3y2iul',
'R9DrOf',
'WQkoQX',
'avuKGt',
'dO875V',
'dSwk4B',
'forum_',
'go3DvF',
'ldpDP2',
'r6wKtc',
's66zoz',
'yQGfVS']
password2 = ['2VSYDo',
'5OTgnD',
'7sQy7Y',
'91ctf_',
'AVfsVk',
'N5K_u8',
'OYyCje',
'PgLPQi',
'aYUJmn',
'c425Xo',
'cePT4s',
'd1zWsP',
'pt05kx',
'rTzw3q']

password3 = ['1Atmmb',
'6XsSGI',
'EXFyUM',
'KWYIiC',
'Qm0jH5',
'Spkdxd',
'TilZRO',
'Uub7HB',
'ZfsjnA',
'cN3O_z',
'com_66',
'dW4quQ',
'kXjpRF',
'lAmNxm',
'n0EmLx',
'r24Q5p',
'rcV0Yl',
'tf_ciJ']

filepath = r'D:\2021\1test\BuuCtf\misc\cjdbmzh' # 解压目录

def breakzip():
    for i in passwd1:
        for j in password2:
            for m in password3:
                payload = i + j + m
                try:
                    z.extractall(path=filepath,pwd=payload.encode('utf-8'))
                    print('成功密钥：',payload)
                    return
                except:
                    print("失败")
# z.extractall(filepath,pwd=b'forum_91ctf_com_66')
breakzip()
z.close()