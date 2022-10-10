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
          <!-- <li>
            <router-link :to="{ path: '/' }"
              class="block py-2 pr-4 pl-3 text-white text-xl md:bg-transparent dark:text-white">
              Home
            </router-link>
          </li>
          <li>
            <router-link :to="{ path: '/about' }"
              class="block py-2 pr-4 pl-3 text-white text-xl md:bg-transparent dark:text-white">
              About Me
            </router-link>
          </li> -->
        </ul>
      </div>
    </div>
  </nav>
  <div class="min-h-screen flex items-start pt-10 justify-center bg-cover bg-[url('https://i.imgur.com/W30ZlbX.png')]">
    <div class="max-w-full bg-slate-900/90 space-y-8 gap-5 rounded-3xl w-4/5 p-10">
      <div>
        <h2
          class=" text-5xl text-center font-bold text-transparent mb-3 pb-3 bg-clip-text bg-gradient-to-r from-blue-500 to-fuchsia-500">
          P-Art Text to Image Generator</h2>
        <h2 class="mt-6 text-center text-2xl text-white">Create art with the powerful Artificial Intelligence</h2>
        <p class="mt-2 text-center text-sm text-gray-600">
        </p>
      </div>

      <div class="flex flex-row gap-6">
        <form class="basis-3/5">

          <div class="rounded-md shadow-sm ">
            <div class="flex items-center">
              <div class="basis-4/5 text-3xl text-white pb-2 font-bold ">Enter word</div>
              <div class="basis-1/5 text-right mr-3 text-xl input-group-addon" v-text="(min + prompt.length+ '/50')">
              </div>
            </div>
            <label for="email-address" class="sr-only">textprompt</label>
            <input id="textprompt" name="text" type="text" autocomplete="text" v-model="prompt" required
              class="appearance-none rounded-3xl text-lg relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900  focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 "
              placeholder="Describe something here" :maxlength="50" />

          </div>
          <div class="overflow-y-auto mt-12 h-80 justify-content-center ">
            <h1 class="text-3xl text-white pb-2 font-bold ">Choose style</h1>
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
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="grid mt-5">
              <div class="flex pb-2 items-center">
                <h1 class="text-3xl text-white font-bold ">Insert Image</h1>
                <h1 class="text-xl text-white ml-5 ">( Optional )</h1>
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
                  <input id="dropzone-file" type="file" class="hidden" accept="image/png, image/jpg, image/jpeg"
                    @change="onFileSelected($event)" />
                </label>
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

        <div class="basis-2/5 grid grid-cols grid-rows justify-center justify-items-center bg-stone-900/90 rounded-3xl">
          <h1
            class="text-4xl  pt-5 font-bold text-transparent mb-3 pb-3 bg-clip-text bg-gradient-to-r from-blue-500 to-fuchsia-500">
            Your artwork</h1>
          <div class="grid bg-base-300 place-items-center border-2 border-violet-700 rounded-3xl "
            style="height: 370px; width: 370px;">

            <div id="loader-bar" name="loader-bar" style="display: none;">
              <loading />
              <h1 class="justify-content-center text-xl">loading...</h1>
            </div>
            <!-- <img src="response"> -->
            <img :src="src" id="imagen" style="display: none">
          </div>
          <button @click="download()" id="download"
            class="btn justify-center px-24 mt-2 rounded-3xl text-white bg-gradient-to-r from-indigo-600 to-fuchsia-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            disabled>
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
import axios from 'axios'
import Loading from './loading.vue'
import { useRouter } from 'vue-router'
import { customAlphabet } from 'nanoid'

const nanoid = customAlphabet('123456789', 6)
export default defineComponent({
  data() {
    return {
      min: 0,
      selectfile: null,
      src: `http://127.0.0.1:8000/gen/generate?lastmod=${nanoid()}`,
    }
  },
  methods: {
    download() {
      axios({
        url: this.src,
        method: "GET",
        responseType: "blob"
      })
        .then((response) => {
          const url = window.URL
            .createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", "Artwork.png");
          document.body.appendChild(link);
          link.click();
        });
    },


  },
  setup() {
    const router = useRouter()
    const prompt: Ref<string> = ref("");
    const selectedStyle: Ref<number> = ref(1);
    const selectedFile: Ref<File | null> = ref(null);
    const IDsession = ref('')

    const onStyleClicked = (styleId: number): void => {
      if (styleId & selectedStyle.value & 1) {
        selectedStyle.value == 1;
        return;
      }
      else {
        selectedStyle.value = styleId;
      }
      console.log(selectedStyle.value);
    };
    const onFileSelected = (ev: Event): void => {
      const target = ev.target as HTMLInputElement

      if (target.files == null) {
        return
      }

      if (target.files.length > 0) {
        if (target.files[0] == null) {
          return
        }
        selectedFile.value = target.files[0]
      }
      console.log('uploading')
    }
    const sendRequest = async () => {
      document.getElementById('loader-bar').style.display = 'block';
      // document.getElementById('imagen').style.display = 'none';
      const idresponse = await ky.post(`http://127.0.0.1:8000/gen`
      ).json<{ massage: string, generated_image_id: string }>()

      IDsession.value = idresponse.generated_image_id

      try {
        const FILEform = new FormData()

        if (selectedFile.value != null) {
          FILEform.append('image', selectedFile.value)
          await ky.post(`http://127.0.0.1:8000/gen/uploadimage/${IDsession.value}`, {
            body: FILEform,
          })
          console.log('success')
        } else {
        }
      } catch (e) {
        console.error(e)
      }

      try {
        if (prompt.value != "") {
          const response = await ky.post(`http://127.0.0.1:8000/gen/generate/${IDsession.value}`, {
            timeout: false,
            json: {
              prompt: prompt.value,
              style: products[selectedStyle.value - 1].imagestyle
            },
            headers: {
              'content-type': 'application/json'
            }
          })
          if (response.status == 200) {
            document.getElementById('loader-bar').style.display = 'none';
            document.getElementById("imagen").style.display = 'block';
            document.getElementById("download").disabled = false;
            const imagefive = document.getElementById("imagen");
            imagefive.src = `http://127.0.0.1:8000/gen/generate?lastmod=${nanoid()}`;
            setTimeout(function () {
              imagefive.src = `http://127.0.0.1:8000/gen/generate?lastmod=${nanoid()}`;
            }, 5000);
            return {
              src: `http://127.0.0.1:8000/gen/generate?lastmod=${nanoid()}`
            }
          }
          return response
        };
      } catch (e) {
        console.error(e)
      }
      router.push({
        name: "display gen image",
        params: {
          generatedImageId: IDsession.value
        }
      })
    };
    return {
      products,
      prompt,
      sendRequest,
      selectedStyle,
      onStyleClicked,
      onFileSelected,
    };
  },
  components: { Loading }
})
</script>
<style>
body {
  margin: 0;
  height: 100%;
  overflow: hidden
}
</style>
