import { ref, computed } from 'vue';
import type { Idioma, Translation } from '../types';

const idioma = ref<Idioma>('pt');

const translations: Record<Idioma, Translation> = {
  pt: {
    header: {
      title: 'Agri Fund Assist',
      subtitle: 'Inclusão bancária inteligente para camponeses'
    },
    chat: {
      title: 'Como posso ajudar hoje?',
      placeholder: 'Digite sua mensagem...',
      send: 'Enviar',
      typing: 'Digitando...'
    },
    services: {
      title: 'Escolha o serviço',
      'abertura-conta': 'Abertura de Conta',
      'credito-agricola': 'Crédito Agrícola',
      'educacao-financeira': 'Educação Financeira',
      'traducao-kimbundu': 'Tradução para Kimbundu',
      'poupanca': 'Conta Poupança',
      'seguros': 'Seguros Agrícolas'
    },
    upload: {
      title: 'Enviar Documento',
      button: 'Escolher Arquivo',
      processing: 'Processando...',
      extracted: 'Texto Extraído'
    }
  },
  en: {
    header: {
      title: 'Agri Fund Assist',
      subtitle: 'Smart banking inclusion for farmers'
    },
    chat: {
      title: 'How can I help you today?',
      placeholder: 'Type your message...',
      send: 'Send',
      typing: 'Typing...'
    },
    services: {
      title: 'Choose service',
      'abertura-conta': 'Account Opening',
      'credito-agricola': 'Agricultural Credit',
      'educacao-financeira': 'Financial Education',
      'traducao-kimbundu': 'Kimbundu Translation',
      'poupanca': 'Savings Account',
      'seguros': 'Agricultural Insurance'
    },
    upload: {
      title: 'Upload Document',
      button: 'Choose File',
      processing: 'Processing...',
      extracted: 'Extracted Text'
    }
  },
  kimbundu: {
    header: {
      title: 'Agri Fund Assist',
      subtitle: 'Kijila kya bank ya muzenza'
    },
    chat: {
      title: 'Kisonga ngi ku salula uyu?',
      placeholder: 'Songa kima kyo...',
      send: 'Tuma',
      typing: 'Kusonga...'
    },
    services: {
      title: 'Sobola kima',
      'abertura-conta': 'Kubula Konta',
      'credito-agricola': 'Kreditu ya Kirimba',
      'educacao-financeira': 'Malongu ma Jindama',
      'traducao-kimbundu': 'Kusolola ku Kimbundu',
      'poupanca': 'Konta ya Kubika',
      'seguros': 'Seguru ya Kirimba'
    },
    upload: {
      title: 'Tuma Papele',
      button: 'Sobola Papele',
      processing: 'Kusolola...',
      extracted: 'Makambu ma Papele'
    }
  },
  umbundu: {
    header: {
      title: 'Agri Fund Assist',
      subtitle: 'Onduli yo bankisi ya vameme'
    },
    chat: {
      title: 'Ngeno ngi ku vanga sino?',
      placeholder: 'Lombela omalovi ayo...',
      send: 'Tuma',
      typing: 'Okulombela...'
    },
    services: {
      title: 'Ofera osilulu',
      'abertura-conta': 'Ovula Conta',
      'credito-agricola': 'Kreditu yo Lima',
      'educacao-financeira': 'Ondjila yo Ndenge',
      'traducao-kimbundu': 'Ovapula ku Kimbundu',
      'poupanca': 'Conta yo Tekela',
      'seguros': 'Seguru yo Lima'
    },
    upload: {
      title: 'Tuma Ekadelu',
      button: 'Ofera Ekadelu',
      processing: 'Ovapula...',
      extracted: 'Omalovi ma Ekadelu'
    }
  },
  kikongo: {
    header: {
      title: 'Agri Fund Assist',
      subtitle: 'Lukalu lwa banki ya bakulu'
    },
    chat: {
      title: 'Nkento ngi ku salusa lelo?',
      placeholder: 'Songa makambu maku...',
      send: 'Fidisa',
      typing: 'Kusonga...'
    },
    services: {
      title: 'Sobola kisalu',
      'abertura-conta': 'Fungola Conta',
      'credito-agricola': 'Kreditu ya Kilima',
      'educacao-financeira': 'Mayela ma Mbongo',
      'traducao-kimbundu': 'Vutudila ku Kimbundu',
      'poupanca': 'Conta ya Bika',
      'seguros': 'Seguru ya Kilima'
    },
    upload: {
      title: 'Fidisa Mukanda',
      button: 'Sobola Mukanda',
      processing: 'Vutudila...',
      extracted: 'Makambu ma Mukanda'
    }
  }
};

export function useTranslations() {
  const t = computed(() => translations[idioma.value]);

  const setIdioma = (novoIdioma: Idioma) => {
    idioma.value = novoIdioma;
  };

  return {
    idioma,
    t,
    setIdioma
  };
}