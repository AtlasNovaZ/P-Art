<template>
<div class="home min-h-screen pt-20 justify bg-cover z-0 overflow-hidden bg-gradient-to-b from-gray-900 via-fuchsia-800 to-blue-900 overflow-y-hidden">
  <div class="grid w-2/4 p-10 grid-cols-2 mx-auto bg-slate-900/60 gap-5 rounded-3xl" style="height: 80vh;">
    <div class="grid grid-row-2">
      <div class="row-span-2">
        <h1 class="text-4xl text-white pb-5 font-bold ">Enter word</h1>
        <input type="text" placeholder="Type word" class="input input-bordered input-info w-full text-xl" />
        <h1 class="text-4xl text-white pb-5 mt-10 font-bold">Style</h1>
      </div>
        <div class="grid grid-cols-3 gap-7 overflow-y-scroll overflow-auto h-80">
          <div class="">
            <img src="https://i.imgur.com/oSPFcub.jpg" class="rounded-3xl"/>
          </div>
          <div class="">
            <img src="https://i.imgur.com/Slf7euk.png" class="rounded-3xl"/>
          </div>
          <div class=" ">
            <img src="https://i.imgur.com/dIahj5z.png" class="rounded-3xl"/>
          </div>
          <div class=" ">
            <img src="https://i.imgur.com/0EJmZnr.png" class="rounded-3xl"/>
          </div>
          <div class=" ">
            <img src="https://i.imgur.com/kWRZ4uU.png" class="rounded-3xl"/>
          </div>
          <div class=" ">
            <img src="https://i.imgur.com/oSPFcub.jpg" class="rounded-3xl"/>
          </div>
          <div class=" ">
            <img src="https://i.imgur.com/oSPFcub.jpg" class="rounded-3xl"/>
          </div>
        </div>
        <div class="pt-5 grid justify-center">
          <div class="flex justify-center items-center w-full">
            <label for="dropzone-file" class="flex flex-col justify-center items-center w-full h-12 px-5 bg-gradient-to-r from-indigo-600 to-fuchsia-600 rounded-lg border-2 border-gray-300 border-dashed cursor-pointer dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                <div class="flex flex-col justify-center items-center pt-5 pb-6">
                    <p class="mb-2 text-sm text-white ">
                      <span class="font-semibold">
                      Click to upload image 
                      </span> 
                      or drag and drop
                    </p>
                    <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG or JPG</p>
                </div>
                <input id="dropzone-file" type="file" class="hidden" />
            </label>
          </div> 
        </div>
        <div class="mt-10 flex justify-center place-content-end">
          <button class="btn shadow-lg shadow-stone-900/50 rounded-3xl bg-gradient-to-r from-indigo-600 to-fuchsia-600 text-white w-full text-xl ">Generate</button>
        
      </div>
    </div>
    <div class="row-span-2 ml-10 ">
      <div class="bg-stone-900 shadow-lg shadow-stone-900/50 border-2 border-indigo-600 w-full h-full rounded-xl"></div>
    </div>
  </div>


</div>

</template>
