# Álbum de Casamento

Este é um projeto de um álbum de casamento digital, desenvolvido em Python com o framework Flask. A aplicação web exibe uma galeria de fotos de casamento de forma elegante e simples.

## Funcionalidades

*   **Galeria de Fotos:** Exibe as fotos do casamento em uma interface web limpa e organizada.
*   **Processamento de Imagens:** Um script auxiliar (`process_images.py`) automatiza o processamento das imagens:
    *   Redimensiona as fotos para um tamanho máximo otimizado para a web.
    *   Adiciona uma moldura personalizável às fotos.
    *   Cria miniaturas (thumbnails) para carregamento rápido da galeria.
*   **Design Responsivo (potencial):** O uso de templates HTML permite a fácil implementação de um design responsivo para visualização em diferentes dispositivos (desktop, tablets, smartphones).

## Como Utilizar

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

*   Python 3.x
*   Pip (gerenciador de pacotes do Python)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio/wedding-album
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *Observação: O arquivo `requirements.txt` está vazio. As dependências `Flask` e `Pillow` precisam ser instaladas manualmente:*
    ```bash
    pip install Flask Pillow
    ```

### Preparando as Imagens

1.  Adicione suas fotos originais na pasta `photos/original`.
2.  Execute o script de processamento de imagens para gerar as versões para a web e as miniaturas:
    ```bash
    python process_images.py
    ```
    As imagens processadas serão salvas em `static/photos` e as miniaturas em `static/photos/thumbs`.

### Executando a Aplicação

1.  Inicie o servidor Flask:
    ```bash
    python app.py
    ```

2.  Abra seu navegador e acesse o seguinte endereço:
    ```
    http://127.0.0.1:5000
    ```

## Estrutura do Projeto

```
.
├── app.py                # Arquivo principal da aplicação Flask
├── process_images.py     # Script para processar as imagens
├── requirements.txt      # Lista de dependências do projeto
├── photos
│   └── original          # Pasta para as fotos originais
├── static
│   └── photos
│       └── thumbs        # Pasta para as miniaturas das fotos
└── templates
    └── album.html        # Template HTML da galeria
```

## Dependências

*   **Flask:** Micro-framework web para Python.
*   **Pillow:** Biblioteca para manipulação de imagens em Python.

## Licença

Este projeto é para fins de demonstração e não possui uma licença específica. Sinta-se à vontade para utilizá-lo e modificá-lo conforme suas necessidades.
