module.exports = {
  title: '慧通物联网云文档中心',
  base: '/',
  locales: {
    '/': {
      lang: 'zh-CN',
      title: '慧通物联网云文档中心'
    }
  },
  head: [
    ['meta', { name: 'keywords', content: 'huitong iot hiot' }],
    ['link', { rel: 'shortcut icon', href: '/images/logo.png' }],
  ],
  themeConfig: {
    logo: '/images/logo.png',
    repo: 'huitong-technologies/docs',
    sideBar: 'auto',
    sidebarDepth: 3,
    locales: {
      '/': {
        selectText: '选择语言',
        label: '简体中文',
        editLinkText: '在 GitHub 上编辑此页',
        serviceWorker: {
          updatePopup: {
            message: "发现新内容可用.",
            buttonText: "刷新"
          }
        },
        nav: [
          { text: '快速入门', link: '/docs/quick-start/' }
        ],
        sidebar: {
          '/docs/': getGuide(),
        }
      }
    }
  },
  serviceWorker: true,
  evergreen: true
}

function getGuide() {
  return [
    'product-intro/',
    'quick-start/',
  ]
}