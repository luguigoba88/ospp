import { TestBed } from '@angular/core/testing';

import { ApiOsppService } from './api-ospp.service';

describe('ApiOsppService', () => {
  let service: ApiOsppService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiOsppService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
