import { TestBed } from '@angular/core/testing';

import { OsppService } from './ospp.service';

describe('OsppService', () => {
  let service: OsppService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OsppService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
