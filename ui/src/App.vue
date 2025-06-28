<script setup lang="ts">
import { ref, nextTick, onMounted } from 'vue';
import { useTranslations } from './composables/useTranslations';
import { useAgriBank } from './composables/useAgriBank';
import type { TipoServico } from './types';

const { idioma, t, setIdioma } = useTranslations();
const { messages, loading, uploading, enviarPergunta, adicionarMensagem, processarUpload } = useAgriBank();

const mensagem = ref('');
const tipoSelecionado = ref<TipoServico>('open-account');
const chatContainer = ref<HTMLElement>();
const fileInput = ref<HTMLInputElement>();
const textoExtraido = ref('');

const scrollToBottom = () => {
  nextTick(() => {
    if (chatContainer.value) {
      chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
    }
  });
};

const enviarMensagem = async () => {
  if (!mensagem.value.trim()) return;

  const perguntaUsuario = mensagem.value;
  adicionarMensagem(perguntaUsuario, 'user', tipoSelecionado.value);
  mensagem.value = '';
  scrollToBottom();

  try {
    console.log(tipoSelecionado.value);

    const resposta = await enviarPergunta(tipoSelecionado.value, perguntaUsuario, idioma.value);
    adicionarMensagem(resposta, 'assistant', tipoSelecionado.value);
    scrollToBottom();
  } catch (error) {
    adicionarMensagem(error.message || 'Desculpe, ocorreu um erro. Tente novamente.', 'assistant');
    scrollToBottom();
  }
};

const handleFileUpload = async (event: Event) => {
  const target = event.target as HTMLInputElement;
  const file = target.files?.[0];

  if (!file) return;

  try {
    adicionarMensagem(`📎 Documento enviado: ${file.name}`, 'user');
    scrollToBottom();

    const texto = await processarUpload(file, idioma.value);
    textoExtraido.value = texto;
    adicionarMensagem(`📄 ${t.value.upload.extracted}:\n\n${texto}`, 'assistant');
    scrollToBottom();
  } catch (error) {
    adicionarMensagem(error.message || 'Erro ao processar documento. Tente novamente.', 'assistant');
    scrollToBottom();
  }

  // Reset file input
  if (fileInput.value) {
    fileInput.value.value = '';
  }
};

const formatarMensagem = (content: string) => {
  return content
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/^\- (.*$)/gim, '• $1')
    .replace(/^(✅|💰|📱|🏪|📊|🎯|📋|💼|🎓|📅|💡|🆓|📞|👥|🌧️|💵|🤝|❌)(.*$)/gim, '<div class="flex items-start gap-2 my-2"><span class="text-lg">$1</span><span>$2</span></div>');
};

onMounted(() => {
  // Mensagem de boas-vindas
  adicionarMensagem(
    `pt: 👋🏾 Olá! Eu sou o Agri Fund Assist, seu assistente digital bancário rural.<br><br>
        en: 👋🏾 Hello! I am Agri Fund Assist, your rural banking digital assistant.<br><br>
        kimbundu: 👋🏾 Ngevu! Mono ke Agri Fund Assist, mudimu wakwetu na banku.<br><br>
        umbundu: 👋🏾 Olá! Ohandi Agri Fund Assist, okapayi koku banku lyoku camponês.<br><br>
        kikongo: 👋🏾 Mbote! Mono ke Agri Fund Assist, mosungi wa banku ya bilanga.`,

      "assistant"
  );
});
</script>

<template>
  <div class="min-h-screen bg-gray-50 flex flex-col">
    <!-- Header -->
    <header class="bg-agri-green-600 text-white shadow-lg">
      <div class="max-w-6xl mx-auto px-4 py-4">
        <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4">
          <div>
            <h1 class="text-2xl font-bold">{{ t.header.title }}</h1>
            <p class="text-agri-green-100 text-sm">{{ t.header.subtitle }}</p>
          </div>
          <select :value="idioma" @change="setIdioma($event.target.value)"
            class="bg-agri-green-700 text-white px-4 py-2 rounded-lg border border-agri-green-500 focus:ring-2 focus:ring-agri-green-300">
            <option value="pt">🇦🇴 Português</option>
            <option value="kimbundu">🗣️ Kimbundu</option>
            <option value="umbundu">🗣️ Umbundu</option>
            <option value="kikongo">🗣️ Kikongo</option>
            <option value="en">🌍 English</option>
          </select>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-1 max-w-4xl mx-auto w-full p-4 flex flex-col gap-6">

      <!-- Service Selection -->
      <div class="bg-white rounded-xl shadow-md p-6 border border-gray-200">
        <h2 class="text-lg font-semibold text-gray-800 mb-4">{{ t.services.title }}</h2>
        <select v-model="tipoSelecionado" class="select-field">
          <option value="open-account">{{ t.services['abertura-conta'] }}</option>
          <option value="agri-credit">{{ t.services['credito-agricola'] }}</option>
          <option value="financial-education">{{ t.services['educacao-financeira'] }}</option>
          <option readonly value="poupanca">{{ t.services['poupanca'] }}</option>
          <option readonly value="seguros">{{ t.services['seguros'] }}</option>
        </select>
      </div>

      <!-- Chat Container -->
      <div class="flex-1 bg-white rounded-xl shadow-md border border-gray-200 flex flex-col">
        <!-- Chat Header -->
        <div class="bg-agri-green-50 rounded-t-xl p-4 border-b border-gray-200">
          <h2 class="text-lg font-semibold text-agri-green-800">{{ t.chat.title }}</h2>
        </div>

        <!-- Messages -->
        <div ref="chatContainer" class="flex-1 p-4 overflow-y-auto max-h-96 space-y-4">
          <TransitionGroup name="slide-up" tag="div" class="space-y-4">
            <div v-for="message in messages" :key="message.id" class="flex"
              :class="message.type === 'user' ? 'justify-end' : 'justify-start'">
              <div :class="message.type === 'user' ? 'chat-bubble-user' : 'chat-bubble-assistant'"
                v-html="formatarMensagem(message.content)" />
            </div>
          </TransitionGroup>

          <!-- Loading indicator -->
          <div v-if="loading" class="flex justify-start">
            <div class="chat-bubble-assistant">
              <div class="flex items-center gap-2">
                <div class="animate-spin h-4 w-4 border-2 border-agri-green-600 border-t-transparent rounded-full">
                </div>
                <span>{{ t.chat.typing }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Message Input -->
        <div class="p-4 border-t border-gray-200">
          <form @submit.prevent="enviarMensagem" class="flex gap-3">
            <input v-model="mensagem" type="text" :placeholder="t.chat.placeholder" class="input-field flex-1"
              :disabled="loading" />
            <button type="submit" :disabled="loading || !mensagem.trim()"
              class="btn-primary disabled:opacity-50 disabled:cursor-not-allowed px-6">
              {{ t.chat.send }}
            </button>
          </form>
        </div>
      </div>

      <!-- File Upload -->
      <div class="bg-black text-white rounded-xl shadow-md p-6">
        <h2 class="text-lg font-semibold mb-4 text-agri-green-100">📎 {{ t.upload.title }}</h2>
        <div class="space-y-4">
          <div class="flex gap-3">
            <input ref="fileInput" type="file" accept=".pdf,.doc,.docx,.txt,.jpg,.png" @change="handleFileUpload"
              class="flex-1 text-sm text-white file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-white file:text-black file:font-medium hover:file:bg-gray-100"
              :disabled="uploading" />
            <div v-if="uploading" class="flex items-center gap-2 text-agri-green-100">
              <div class="animate-spin h-4 w-4 border-2 border-agri-green-300 border-t-transparent rounded-full"></div>
              <span class="text-sm">{{ t.upload.processing }}</span>
            </div>
          </div>

          <div v-if="textoExtraido" class="bg-agri-green-900 p-4 rounded-lg text-agri-green-100">
            <h3 class="font-semibold mb-2">📝 {{ t.upload.extracted }}:</h3>
            <pre class="whitespace-pre-wrap text-sm">{{ textoExtraido }}</pre>
          </div>
        </div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white text-center py-4 text-sm">
      <div class="max-w-4xl mx-auto px-4">
        <p>© 2024 Agri Fund Assist - Inclusão bancária inteligente para todos</p>
      </div>
    </footer>
  </div>
</template>