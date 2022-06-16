module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      backgroundImage: {
        'hero-pattern': "url('https://i.imgur.com/Slf7euk.png')",
        'footer-texture': "url('https://i.imgur.com/dIahj5z.png')",
      },
    },
  },
  plugins: [
    require('daisyui')
  ],
}

