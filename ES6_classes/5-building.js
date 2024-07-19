export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new TypeError('Cannot construct Building instances directly');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (typeof newSqft !== 'number') {
      throw new TypeError('New value must be a number');
    }
    this._sqft = newSqft;
  }

  /* eslint-disable class-methods-use-this */
  evecuationWarningMessage() {
    throw new Error('Class extending Building must override evecuationWarningMessage');
  }
}
/* eslint-enable class-methods-use-this */
