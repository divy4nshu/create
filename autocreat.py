
import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))