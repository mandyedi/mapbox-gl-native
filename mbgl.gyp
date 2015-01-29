{
  'includes': [
    './gyp/common.gypi',
    './gyp/shaders.gypi',
    './gyp/version.gypi',
    './gyp/styles.gypi',
    './gyp/certificates.gypi',
    './gyp/standalone.gypi',
    './gyp/core.gypi',
    './gyp/none.gypi',
  ],
  'conditions': [
    ['headless_lib == "cgl"', { 'includes': [ './gyp/headless-cgl.gypi' ] } ],
    ['headless_lib == "glx"', { 'includes': [ './gyp/headless-glx.gypi' ] } ],
    ['platform_lib == "osx"', { 'includes': [ './gyp/platform-osx.gypi' ] } ],
    ['platform_lib == "ios"', { 'includes': [ './gyp/platform-ios.gypi' ] } ],
    ['platform_lib == "linux"', { 'includes': [ './gyp/platform-linux.gypi' ] } ],
    ['platform_lib == "android"', { 'includes': [ './gyp/platform-android.gypi' ] } ],
    ['http_lib == "curl"', { 'includes': [ './gyp/http-curl.gypi' ] } ],
    ['http_lib == "nsurl"', { 'includes': [ './gyp/http-nsurl.gypi' ] } ],
    ['asset_lib == "fs"', { 'includes': [ './gyp/asset-fs.gypi' ] } ],
    ['asset_lib == "zip"', { 'includes': [ './gyp/asset-zip.gypi' ] } ],
    ['cache_lib == "sqlite"', { 'includes': [ './gyp/cache-sqlite.gypi' ] } ],
  ],
}
