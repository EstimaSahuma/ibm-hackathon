<template>
  <div class="min-h-screen bg-white text-black font-sans">
    <header class="bg-green-600 text-white py-4 px-6 shadow-md flex flex-col sm:flex-row sm:justify-between sm:items-center">
      <div>
        <h1 class="text-2xl font-bold">Agri Fund Assist</h1>
        <p class="text-sm">Inclusão bancária inteligente para camponeses</p>
      </div>
      <select v-model="idioma" class="mt-2 sm:mt-0 bg-green-700 text-white px-3 py-1 rounded">
        <option value="pt">🇦🇴 Português</option>
        <option value="kimbundu">🗣️ Kimbundu</option>
        <option value="umbundu">🗣️ Umbundu</option>
        <option value="kikongo">🗣️ Kikongo</option>
        <option value="en">🌍 English</option>
      </select>
    </header>

    <main class="p-6 grid gap-6 max-w-3xl mx-auto">
      <section class="bg-green-50 border border-green-200 p-5 rounded-xl shadow">
        <h2 class="text-xl font-semibold mb-4 text-green-900">📝 Enviar Pergunta</h2>
        <form @submit.prevent="enviarPergunta" class="grid gap-4">
          <div>
            <label class="block mb-1 text-sm font-medium text-green-800">Tipo de serviço</label>
            <select v-model="tipo" class="w-full p-2 rounded border-green-400">
              <option value="abertura-conta">Abertura de Conta</option>
              <option value="credito-agricola">Crédito Agrícola</option>
              <option value="educacao-financeira">Educação Financeira</option>
              <option value="traducao-kimbundu">Tradução para Kimbundu</option>
            </select>
          </div>

          <div>
            <label class="block mb-1 text-sm font-medium text-green-800">Mensagem</label>
            <textarea v-model="mensagem" class="w-full p-2 rounded border-green-400" rows="4" placeholder="Digite aqui..."></textarea>
          </div>

          <button class="bg-green-700 text-white px-4 py-2 rounded hover:bg-green-800 flex items-center gap-2 justify-center" type="submit">
            <span v-if="!loading">Enviar</span>
            <span v-else class="animate-spin border-2 border-white border-t-transparent rounded-full w-4 h-4"></span>
          </button>
        </form>
      </section>

      <section class="bg-white border border-green-300 p-5 rounded-xl shadow" v-if="resposta">
        <h2 class="text-xl font-semibold mb-3 text-green-900">📬 Resposta</h2>
        <div class="bg-green-100 text-green-900 p-4 rounded-lg whitespace-pre-wrap">
          {{ resposta }}
        </div>
      </section>

      <section class="bg-black text-white p-5 rounded-xl shadow">
        <h2 class="text-xl font-semibold mb-3 text-green-100">📎 Upload de Documento</h2>
        <form @submit.prevent="uploadDocumento" class="grid gap-3">
          <input type="file" @change="onFileChange" class="text-sm text-black bg-white p-2 rounded border" />
          <button class="bg-white text-black px-4 py-2 rounded hover:bg-gray-200 flex items-center gap-2 justify-center" type="submit">
            <span v-if="!uploading">Enviar Documento</span>
            <span v-else class="animate-spin border-2 border-black border-t-transparent rounded-full w-4 h-4"></span>
          </button>
        </form>
        <div v-if="textoExtraido" class="mt-4 bg-green-900 p-4 rounded text-green-100">
          <h3 class="font-semibold">📝 Texto Extraído:</h3>
          <p class="whitespace-pre-wrap">{{ textoExtraido }}</p>
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
    resposta.value = '❌ Erro ao enviar mensagem.'
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
  font-family: 'Segoe UI', sans-serif;
}

@media (max-width: 640px) {
  main {
    padding: 1rem;
  }
  header {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
