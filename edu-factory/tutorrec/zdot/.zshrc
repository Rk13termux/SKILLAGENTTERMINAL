# zshrc de grabación edu-factory: p10k profesional, fondo negro #000000
# Se carga con ZDOTDIR en el PTY de asciinema (no toca tu ~/.zshrc diario).

export POWERLEVEL9K_INSTANT_PROMPT=off

# Sin '%' EOL de zsh/p10k tras comandos
typeset -g PROMPT_EOL_MARK=''
typeset -g POWERLEVEL9K_PROMPT_EOL_MARK=''
unsetopt prompt_sp

# Sin prompts interactivos de oh-my-zsh (actualizaciones, compfix...)
export DISABLE_AUTO_UPDATE="true"
export ZSH_DISABLE_COMPFIX="true"
zstyle ':omz:update' mode disabled
zstyle ':completion:*' use-cache yes

export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"
# Sin autosuggestions: el texto fantasma ensucia la grabación
plugins=(git sudo history extract)
source "$ZSH/oh-my-zsh.sh"

[[ -f "$HOME/.p10k.zsh" ]] && source "$HOME/.p10k.zsh"

# Fondo negro puro (color 000) en el theme y en todos los segmentos p10k
for _seg in POWERLEVEL9K_BACKGROUND POWERLEVEL9K_LEFT_PROMPT_BACKGROUND \
  POWERLEVEL9K_RIGHT_PROMPT_BACKGROUND POWERLEVEL9K_SEGMENT_SEPARATOR_BACKGROUND \
  POWERLEVEL9K_MULTILINE_FIRST_PROMPT_GAP_BACKGROUND \
  POWERLEVEL9K_MULTILINE_NEWLINE_PROMPT_GAP_BACKGROUND \
  POWERLEVEL9K_LEFT_PROMPT_END_SEPARATOR_BACKGROUND \
  POWERLEVEL9K_PROMPT_CHAR_BACKGROUND POWERLEVEL9K_OS_ICON_BACKGROUND \
  POWERLEVEL9K_CONTEXT_BACKGROUND POWERLEVEL9K_DIR_BACKGROUND \
  POWERLEVEL9K_VCS_BACKGROUND POWERLEVEL9K_STATUS_BACKGROUND \
  POWERLEVEL9K_TIME_BACKGROUND POWERLEVEL9K_COMMAND_EXECUTION_TIME_BACKGROUND; do
  typeset -g "${_seg}"=000
done

# Prompt derecho vacío: el reloj se repinta y pisa la línea mientras se teclea
typeset -g POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()

# Prompt multi-línea limpio de tu config
typeset -g POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX='%238F╭─'
typeset -g POWERLEVEL9K_MULTILINE_LAST_PROMPT_PREFIX='%238F╰─%F{076}❯%f '
typeset -g POWERLEVEL9K_PROMPT_ADD_NEWLINE=false
typeset -g POWERLEVEL9K_TRANSIENT_PROMPT=off

EDITOR=nano
alias ls='ls --color=auto'
alias ll='ls -la --color=auto'

# Fondo de terminal explícito negro (si el emulador lo respeta)
printf '\e]11;#000000\e\\'