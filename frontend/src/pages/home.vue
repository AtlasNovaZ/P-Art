<template>
  <nav class="z-100 bg-stone-900 shadow-lg  border-b-4 border-indigo-600 overflow-y-hidden">
    <div class="container flex flex-wrap justify-between py-3 items-center mx-auto shadow-lg  ">
      <a href="#" class="flex items-center">
        <h1
          class="text-4xl self-center font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-500  to-fuchsia-500">
          P-Art</h1>
      </a>
      <div class="hidden w-full md:block md:w-auto" id="mobile-menu">
        <ul class="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium">
          <li>
            <router-link :to="{ path: '/' }"
              class="block py-2 pr-4 pl-3 text-white text-xl md:bg-transparent dark:text-white">
              Home
            </router-link>
          </li>
          <li>
            <router-link :to="{ path: '/about' }"
              class="block py-2 pr-4 pl-3 text-white text-xl md:bg-transparent dark:text-white">
              About
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <div
    class="min-h-screen flex items-start pt-10 bg-gradient-to-b from-gray-900 via-fuchsia-800 to-blue-900 justify-center ">
    <div class="max-w-full bg-slate-900/60 space-y-8 gap-5 rounded-3xl w-4/5 p-10">
      <div>

        <h2
          class=" text-5xl text-center font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-500 to-fuchsia-500">
          P-Art Text to Image Generator</h2>
        <h2 class="mt-6 text-center text-2xl text-white">test text2image</h2>
        <p class="mt-2 text-center text-sm text-gray-600">
        </p>
      </div>

      <div class="flex flex-row gap-6">
        <form class="basis-3/5">

          <div class="rounded-md shadow-sm ">
            <div>
              <h1 class="text-2xl text-white pb-2 font-bold ">Enter word</h1>
              <label for="email-address" class="sr-only">textprompt</label>
              <input id="textprompt" name="text" type="text" autocomplete="text" required v-model="prompt"
                class="appearance-none rounded-3xl text-lg relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900  focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 "
                placeholder="Describe something here" />
            </div>
          </div>
          <div class="overflow-y-auto mt-12 h-80 justify-content-center ">
            <h1 class="text-2xl text-white pb-2 font-bold ">Choose style</h1>
            <div class="grid grid-cols-5 gap-5 px-5">
              <div v-for="product in products">
                <div :key="product.id" :class="selectedStyle != product.id ?
                  'group relative' : 'group relative border-4 border-purple-700 rounded-2xl hover:bg-purple-400'
                " @click.native="onStyleClicked(product.id)">
                  <div
                    class="w-full min-h-80 bg-gray-200 aspect-w-1 aspect-h-1 rounded-xl overflow-hidden group-hover:opacity-80 lg:aspect-none">
                    <img :src="product.imageSrc" class="w-full h-full object-center object-cover lg:w-full lg:h-full" />
                  </div>
                  <div class="mt-2 flex justify-center">
                    <div>
                      <h3 class="text-lg text-white justify-center">
                        <a>
                          <span aria-hidden="true" class="absolute inset-0" />
                          {{ product.name }}
                        </a>
                      </h3>
                      <!-- <p class="mt-1 text-sm text-gray-500">{{ product.color }}</p> -->
                    </div>

                  </div>
                </div>
              </div>
            </div>
            <div class="grid mt-5">
              <div class="flex pb-2">
                <h1 class="text-4xl text-white font-bold ">Insert Image</h1>
                <h1 class="text-lg text-white ml-5 ">Optional</h1>
              </div>
              <div class="flex justify-center justify-items-center w-80 ">
                <label for="dropzone-file"
                  class="grid grid-col justify-center justify-items-center w-full h-25 bg-gray-50 rounded-lg border-2 border-gray-300  cursor-pointer dark:hover:bg-bray-800 dark:bg-purple-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                  <div class="flex flex-col justify-center items-center pt-4 pb-6">
                    <p class="mb-2 text-md text-white "><span class="font-semibold">Upload
                        Image</span>
                    </p>
                    <p class="text-xs text-white">PNG, JPEG, JPG</p>
                  </div>
                  <!-- <input id="dropzone-file" type="file" class="hidden" accept="image/png, image/jpg, image/jpeg"
                    @change="onFileSelected($event)" /> -->
                </label>
                <!-- <input id="dropzone-file" type="file" @change="onFileSelected($event)" /> -->
              </div>
            </div>

          </div>

          <div>
            <button @click.prevent="sendRequest()"
              class="group relative w-full flex justify-center py-2 mt-6 px-4 border border-transparent text-sm font-medium rounded-3xl text-white bg-gradient-to-r from-indigo-600 to-fuchsia-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
              <span
                class="absolute left-0 inset-y-0 flex items-center pl-3 h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
                aria-hidden="true">
              </span>
              <h1 class="text-2xl text-white font-bold ">Generate</h1>
            </button>
          </div>
        </form>


        <div class="basis-2/5 grid grid-cols grid-rows justify-center justify-items-center bg-slate-900/80 rounded-3xl">
          <h1 class="text-4xl text-white pt-5 font-bold ">Your artwork</h1>
          <!-- <img src="" class=" bg-gray-100 rounded-lg animate-spin" /> -->
          <!-- <img src="http://localhost:8000/gen?lastmod=12345678" /> -->
          <img :src="src">


          <!-- <div>
            <button class="btn btn-square loading p-20 rounded-2xl bg-purple-400"></button>
          </div> -->
          <button @click="download()"
            class="justify-center px-11 mt-2 m-3 b rounded-3xl text-white bg-gradient-to-r from-indigo-600 to-fuchsia-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">

            <h1 class="text-xl text-white font-bold ">Download</h1>
          </button>

        </div>
      </div>
    </div>
  </div>


</template>

<script lang="ts">
import { products } from '../constants'
import { ref, Ref, defineComponent } from 'vue'
import ky from 'ky'
import axios from 'axios';





export default defineComponent({
  setup() {
    const prompt: Ref<string> = ref('')
    const selectedStyle: Ref<number> = ref(1)
    // const styles: Ref<string> = ref(products[3].imagestyle)
    const selectedFile: Ref<File | null> = ref(null)

    const returnedImage: Ref<Blob | null> = ref(null)

    const onStyleClicked = (styleId: number): void => {
      if (styleId & selectedStyle.value & 1) {
        selectedStyle.value == 1
        return
      } else {
        selectedStyle.value = styleId
      }
      console.log(selectedStyle.value)

    }
    // const onFileSelected = (ev: Event) => {
    //   console.log(ev)
    //   console.log('upload pass')
    //   const target = ev.target as HTMLInputElement
    //   selectedFile.value = target.files == null ? null : target.files[0]

    // }

    const sendRequest = async () => {



      // var ws = new WebSocket("ws://localhost:8000/ws");
      // ws.onmessage = function (event) {

      // };
      // function sendMessage(event) {
      //   var input = document.getElementById("messageText")
      //   ws.send(input.value)
      //   input.value = ''
      //   event.preventDefault()
      // }
      // if (selectedFile.value == null) {
      //   return
      // }

      // const image = new FormData()
      // image.append('base_image', selectedFile.value, selectedFile.value.toString())

      // const form = new FormData()
      // // form.append('base_image', selectedFile.value, selectedFile.value.toString())
      // form.append('prompt_text', prompt.value)
      // form.append('style', products.values.toString())

      const response = await ky.post('http://127.0.0.1:8000/gen', {
        onDownloadProgress: (progress, chunk) => {
          // Example output:
          // `0% - 0 of 1271 bytes`
          // `100% - 1271 of 1271 bytes`
          console.log(`${progress.percent * 100}% - ${progress.transferredBytes} of ${progress.totalBytes} bytes`);
        },
        timeout: false,
        json: {
          prompt: prompt.value,
          style: products[selectedStyle.value - 1].imagestyle
        }
      }).json()

      // const responseimage = await ky.get('http://localhost:8000/gen', {
      //   body: image
      // }).json()

      console.log(response)
      // console.log(responseimage)

      const imagedresponse = await ky.get('http://localhost:8000/gen', {
      }).blob();

      console.log(imagedresponse)
      // returnedImage.value = imagedresponse

    }



    return {
      products,
      prompt,
      sendRequest,
      onStyleClicked,
      selectedStyle,
      // selectedFile,
      //onFileSelected,
      returnedImage
    }
  },
  data() {
    return {
      src: "http://localhost:8000/gen?lastmod=12345678"
    }
  },
  methods: {
    callFunction: function () {
      let i = 0;
      var v = this;
      setInterval(() => {
        this.src = this.src[i];
        if (++i === this.src.length) i = 0;
        v.src = "http://localhost:8000/gen?lastmod=12345678"
      }, 1000);
    },
    download() {
      axios({
        url: 'http://localhost:8000/gen?lastmod=12345678',
        method: 'GET',
        responseType: 'blob'
      })
        .then((response) => {
          const url = window.URL
            .createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', 'image.png');
          document.body.appendChild(link);
          link.click();
        })
    },


  },

  mounted() {
    this.callFunction()
  }

})
</script>
