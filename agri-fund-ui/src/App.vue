<template>
  <div class="min-h-screen bg-white text-black font-sans">
    <header
      class="bg-green-600 text-white py-4 px-6 shadow-md flex flex-col sm:flex-row sm:justify-between sm:items-center">
      <div>
        <h1 class="text-2xl font-bold">AgriBank Assist</h1>
        <p class="text-sm">Inclusão bancária inteligente para camponeses</p>
      </div>
      <select v-model="idioma" class="mt-2 sm:mt-0 bg-green-700 text-white px-3 py-1 rounded">
        <option value="pt">Português</option>
        <option value="kimbundu">Kimbundu</option>
        <option value="umbundu">Umbundu</option>
        <option value="kikongo">Kikongo</option>
      </select>
    </header>

    <main class="p-6 grid gap-6">
      <section class="bg-green-100 p-4 rounded-xl">
        <h2 class="text-lg font-semibold mb-2">Enviar Pergunta</h2>
        <form @submit.prevent="enviarPergunta">
          <label class="block mb-1 text-sm font-medium">Tipo de serviço</label>
          <select v-model="tipo" class="w-full p-2 rounded border mb-3">
            <option value="abertura-conta">Abertura de Conta</option>
            <option value="credito-agricola">Crédito Agrícola</option>
            <option value="educacao-financeira">Educação Financeira</option>
            <option value="traducao-kimbundu">Tradução para Kimbundu</option>
          </select>

          <label class="block mb-1 text-sm font-medium">Mensagem</label>
          <textarea v-model="mensagem" class="w-full p-2 rounded border mb-3" rows="4"></textarea>

          <button class="bg-green-700 text-white px-4 py-2 rounded hover:bg-green-800 flex items-center gap-2"
            type="submit">
            <span v-if="!loading">Enviar</span>
            <span v-else class="animate-spin border-2 border-white border-t-transparent rounded-full w-4 h-4"></span>
          </button>
        </form>
      </section>

      <section class="bg-green-50 p-4 rounded-xl" v-if="resposta">
        <h2 class="text-lg font-semibold mb-2">Resposta</h2>
        <p>{{ resposta }}</p>
      </section>

      <section class="bg-black text-white p-4 rounded-xl">
        <h2 class="text-lg font-semibold mb-2">Upload de Documento</h2>
        <form @submit.prevent="uploadDocumento">
          <input type="file" @change="onFileChange" class="mb-2 text-black" />
          <button class="bg-white text-black px-4 py-2 rounded hover:bg-gray-200 flex items-center gap-2" type="submit">
            <span v-if="!uploading">Enviar Documento</span>
            <span v-else class="animate-spin border-2 border-black border-t-transparent rounded-full w-4 h-4"></span>
          </button>
        </form>
        <div v-if="textoExtraido" class="mt-3 text-green-200">
          <h3 class="font-semibold">Texto Extraído:</h3>
          <p>{{ textoExtraido }}</p>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const mensagem = ref('')
const tipo = ref('abertura-conta')
const resposta = ref('')
const selectedFile = ref(null)
const textoExtraido = ref('')
const idioma = ref('pt')
const loading = ref(false)
const uploading = ref(false)

const enviarPergunta = async () => {
  try {
    loading.value = true
    const formData = new FormData()
    formData.append('msg', mensagem.value)
    formData.append('idioma', idioma.value)
    if (tipo.value === 'educacao-financeira') {
      formData.delete('msg')
      formData.append('topico', mensagem.value)
    }

    const { data } = await axios.post(`http://localhost:8000/${tipo.value}/`, formData)
    resposta.value = data.resposta || data.traducao
  } catch (e) {
    resposta.value = 'Erro ao enviar mensagem.'
  } finally {
    loading.value = false
  }
}

const onFileChange = (e) => {
  selectedFile.value = e.target.files[0]
}

const uploadDocumento = async () => {
  if (!selectedFile.value) return
  try {
    uploading.value = true
    const formData = new FormData()
    formData.append('file', selectedFile.value)
    const { data } = await axios.post('http://localhost:8000/upload-documento/', formData)
    textoExtraido.value = data.texto_extraido
  } finally {
    uploading.value = false
  }
}
</script>

<style>
body {
  background-color: #ffffff;
  color: #000000;
}

@media (max-width: 640px) {
  main {
    padding: 1rem;
  }
}
</style>
