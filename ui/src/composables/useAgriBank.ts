import { ref } from 'vue';
import axios from 'axios';
import type { Message, TipoServico } from '../types';

const messages = ref<Message[]>([]);
const loading = ref(false);
const uploading = ref(false);

export function useAgriBank() {
  
  const enviarPergunta = async (tipo: TipoServico, pergunta: string, idioma: string): Promise<string> => {
    loading.value = true;
    
    try {
      const formData = new FormData();
      
      if (tipo === 'educacao-financeira') {
        formData.append('topico', pergunta);
      } else {
        formData.append('msg', pergunta);
      }
      
      formData.append('lang', idioma);
      
      const { data } = await axios.post(`http://localhost:8000/${tipo}/`, formData);
      return data.response || data.traducao || 'Resposta recebida com sucesso.';
      
    } catch (error) {
      console.error('Erro na API:', error);
      throw new Error('❌ Erro ao enviar mensagem. Verifique sua conexão.');
    } finally {
      loading.value = false;
    }
  };

  const adicionarMensagem = (content: string, type: 'user' | 'assistant', serviceType?: TipoServico) => {
    const message: Message = {
      id: Date.now().toString(),
      content,
      type,
      timestamp: new Date(),
      serviceType
    };
    messages.value.push(message);
  };

  const processarUpload = async (file: File, idioma: string): Promise<string> => {
    uploading.value = true;
    
    try {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('lang', idioma);
      
      const { data } = await axios.post('http://localhost:8000/upload-documento/', formData);
      return data.texto_extraido || 'Documento processado com sucesso.';
      
    } catch (error) {
      console.error('Erro no upload:', error);
      throw new Error('❌ Erro ao processar documento.');
    } finally {
      uploading.value = false;
    }
  };

  return {
    messages,
    loading,
    uploading,
    enviarPergunta,
    adicionarMensagem,
    processarUpload
  };
}