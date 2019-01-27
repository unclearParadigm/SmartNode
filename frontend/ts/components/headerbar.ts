class Headerbar { 
    private readonly navbarImage: string = '/static/img/smartnode.png';
    private readonly navbarLink: string = 'https://github.com/unclearParadigm/SmartNode';

    private backendVersion: string = 'Unknown';

    constructor() { }

    public setBackendVersion(backendVersion: string) {
        this.backendVersion = backendVersion;
    }

    public render(): string {
        return `
        <nav class="navbar" role="navigation" aria-label="main navigation">
            <div class="navbar-brand">
                <a class="navbar-item" href="${this.navbarLink}">
                    <img src="${this.navbarImage}"/>
                </a>
            </div>
      
            <div class="navbar-menu">
                <div class="navbar-start">
                    <a class="navbar-item">Home</a>
                    <a class="navbar-item">Documentation</a>
                </div>
                <div class="navbar-end">
                    <div class="navbar-item">
                        <a class="button is-success is-outlined">${this.backendVersion}</a>
                    </div>
                </div>
            </div>
        </nav>`;
    }
}