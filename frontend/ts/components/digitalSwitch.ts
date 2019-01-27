class DigitalSwitch {
    private gpioState: GPIOState | null;

    constructor(
        private readonly container: JQuery,
        private readonly dataService: DataProviderService, 
        private readonly gpioConfiguration: GPIOConfiguration,
        private readonly switchUpdateInterval: number) {
        
        this.gpioState = null;
        this.render();
    }

    public start(): void {
        setInterval(() => {
            this.dataService.fetchGPIOState(this.gpioConfiguration.gpio, (newGPIOState) => {
                this.gpioState = newGPIOState;
                this.render();
                $(`#js-digitalswitch-${this.gpioConfiguration.gpio}`).change(() => {
                    this.invertState();
                });
            });
            this.container.html(this.render());
        }, this.switchUpdateInterval);
    }

    public invertState(): void {
        console.log("STATE CHANGE DETECTED ... POSTING TO SERVICE");
    }

    public render(): string {
        var subTemplate;
        if(this.gpioState === null) {
            subTemplate = `
            <div class="sk-folding-cube">
                <div class="sk-cube1 sk-cube"></div>
                <div class="sk-cube2 sk-cube"></div>
                <div class="sk-cube4 sk-cube"></div>
                <div class="sk-cube3 sk-cube"></div>
            </div>`
        } else {
            const toggleChecked = this.gpioState.high ? 'checked="checked"' : '';
            subTemplate = `
            <div class="field">
                <input id="js-digitalswitch-${this.gpioConfiguration.gpio}" type="checkbox" name="switchLarge" class="switch is-large is-success" ${toggleChecked}>
                <label for="js-digitalswitch-${this.gpioConfiguration.gpio}"></label>
            </div>`;
        }

        return `<div class="column card has-text-centered js-digitalswitch-${this.gpioConfiguration.gpio}" style="maring: 10px;">
            <header class="card-header">
            <p class="card-header-title">${this.gpioConfiguration.name}</p>
            <a href="#" class="card-header-icon" aria-label="more options">
                <span class="icon">
                <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
            </a>
            </header>
            <div class="card-content">
                <div class="content">
                    ${this.gpioConfiguration.mode} ${this.gpioConfiguration.direction}
                </div>
                <div class="content">
                    ${subTemplate}
                </div>
            </div>
            <footer class="card-footer">
            <a href="#" class="card-footer-item">Save</a>
            <a href="#" class="card-footer-item">Edit</a>
            <a href="#" class="card-footer-item">Delete</a>
            </footer>
        </div>`;
    }
}