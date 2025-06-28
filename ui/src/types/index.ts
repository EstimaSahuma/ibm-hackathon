export interface Message {
  id: string;
  content: string;
  type: 'user' | 'assistant';
  timestamp: Date;
  serviceType?: TipoServico;
}

export interface UploadedFile {
  name: string;
  content: string;
  extractedText?: string;
}

export type TipoServico = 
  | 'open-account'
  | 'agri-credit'
  | 'financial-education'
  | 'poupanca'
  | 'seguros';

export type Idioma = 'pt' | 'kimbundu' | 'umbundu' | 'kikongo' | 'en';

export interface Translation {
  header: {
    title: string;
    subtitle: string;
  };
  chat: {
    title: string;
    placeholder: string;
    send: string;
    typing: string;
  };
  services: {
    title: string;
    'abertura-conta': string;
    'credito-agricola': string;
    'educacao-financeira': string;
    'traducao-kimbundu': string;
    'poupanca': string;
    'seguros': string;
  };
  upload: {
    title: string;
    button: string;
    processing: string;
    extracted: string;
  };
}